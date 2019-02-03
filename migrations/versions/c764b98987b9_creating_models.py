"""Creating models

Revision ID: c764b98987b9
Revises: 
Create Date: 2019-02-03 02:16:10.689731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c764b98987b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course',
    sa.Column('cprefix', sa.String(length=40), nullable=True),
    sa.Column('cno', sa.Integer(), nullable=False),
    sa.Column('ctitle', sa.String(length=50), nullable=True),
    sa.Column('chours', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('cno')
    )
    op.create_table('student',
    sa.Column('sid', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('fname', sa.String(length=20), nullable=False),
    sa.Column('lname', sa.String(length=20), nullable=False),
    sa.Column('address1', sa.String(length=40), nullable=True),
    sa.Column('address2', sa.String(length=40), nullable=True),
    sa.Column('city', sa.String(length=40), nullable=True),
    sa.Column('state', sa.String(length=40), nullable=True),
    sa.Column('zip', sa.Integer(), nullable=True),
    sa.Column('sType', sa.String(length=5), nullable=True),
    sa.Column('majorDept', sa.String(length=4), nullable=True),
    sa.Column('gradAssistant', sa.String(length=1), nullable=True),
    sa.PrimaryKeyConstraint('email'),
    sa.UniqueConstraint('sid')
    )
    op.create_table('section',
    sa.Column('term', sa.String(length=2), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('crn', sa.Integer(), nullable=False),
    sa.Column('cprefix', sa.String(length=4), nullable=True),
    sa.Column('cno', sa.Integer(), nullable=True),
    sa.Column('days', sa.String(length=6), nullable=True),
    sa.Column('starttime', sa.String(length=5), nullable=True),
    sa.Column('endtime', sa.String(length=5), nullable=True),
    sa.Column('room', sa.String(length=10), nullable=True),
    sa.Column('cap', sa.Integer(), nullable=True),
    sa.Column('instructor', sa.String(length=30), nullable=True),
    sa.Column('auth', sa.String(length=1), nullable=True),
    sa.Column('course_cpcrn', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_cpcrn'], ['course.cno'], ),
    sa.PrimaryKeyConstraint('crn')
    )
    op.create_table('enroll',
    sa.Column('sid', sa.Integer(), nullable=False),
    sa.Column('term', sa.String(length=2), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('crn', sa.Integer(), nullable=True),
    sa.Column('grade', sa.String(length=2), nullable=True),
    sa.Column('student_sid', sa.String(length=40), nullable=True),
    sa.Column('section_tyc', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['section_tyc'], ['section.crn'], ),
    sa.ForeignKeyConstraint(['student_sid'], ['student.email'], ),
    sa.PrimaryKeyConstraint('sid'),
    sa.UniqueConstraint('term')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('enroll')
    op.drop_table('section')
    op.drop_table('student')
    op.drop_table('course')
    # ### end Alembic commands ###
